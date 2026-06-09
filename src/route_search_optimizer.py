```python
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from heapq import heappop, heappush
from math import inf
from typing import Dict, FrozenSet, Iterable, Mapping, Tuple


@dataclass(frozen=True)
class Edge:
    """
    İki durak arasındaki yol bilgisini tutar.

    target: Gidilecek durak
    distance_km: Yol mesafesi
    base_minutes: Trafik yokken ortalama süre
    traffic_factor: Trafik yoğunluğu katsayısı
    is_closed: Yol kapalıysa True olur
    """
    target: str
    distance_km: float
    base_minutes: float
    traffic_factor: float = 1.0
    is_closed: bool = False


@dataclass(frozen=True)
class RouteResult:
    """
    Optimum rota sonucunu tutar.
    """
    path: Tuple[str, ...]
    total_minutes: float
    total_distance_km: float
    total_cost: float
    visited_nodes: int


class RouteSearchOptimizer:
    """
    Akıllı Ulaşım Sistemi için optimize edilmiş rota arama sınıfı.

    Yapılan optimizasyonlar:
    - Gereksiz rota kopyalama azaltıldı.
    - Priority Queue kullanılarak arama hızı artırıldı.
    - Daha önce hesaplanan rotalar cache ile saklandı.
    - Kapalı yollar arama sırasında elendi.
    - Kullanılamayan duraklar blocked_nodes ile dışarıda bırakıldı.
    - Bellek kullanımı için tuple tabanlı grafik yapısı kullanıldı.
    """

    def __init__(self, graph: Mapping[str, Iterable[Edge]]):
        self.graph: Dict[str, Tuple[Edge, ...]] = {
            node: tuple(edges) for node, edges in graph.items()
        }

        self.nodes = set(self.graph.keys())

        for edges in self.graph.values():
            for edge in edges:
                self.nodes.add(edge.target)

    def _edge_cost(self, edge: Edge) -> float:
        """
        Yol maliyetini süre, trafik yoğunluğu ve mesafeye göre hesaplar.
        """
        traffic_factor = max(edge.traffic_factor, 0.1)
        traffic_minutes = edge.base_minutes * traffic_factor
        distance_penalty = edge.distance_km * 0.05

        return traffic_minutes + distance_penalty

    @lru_cache(maxsize=256)
    def shortest_path(
        self,
        start: str,
        end: str,
        blocked_nodes: FrozenSet[str] = frozenset()
    ) -> RouteResult:
        """
        Başlangıç ve hedef durak arasında en uygun rotayı bulur.
        """

        if start not in self.nodes:
            raise ValueError(f"Bilinmeyen başlangıç durağı: {start}")

        if end not in self.nodes:
            raise ValueError(f"Bilinmeyen hedef durağı: {end}")

        if start == end:
            return RouteResult(
                path=(start,),
                total_minutes=0.0,
                total_distance_km=0.0,
                total_cost=0.0,
                visited_nodes=1
            )

        distances = {start: 0.0}
        minutes = {start: 0.0}
        kilometers = {start: 0.0}
        previous = {}

        queue = []
        counter = 0
        visited_nodes = 0

        heappush(queue, (0.0, counter, start))

        while queue:
            current_cost, _, current_node = heappop(queue)

            if current_cost > distances.get(current_node, inf):
                continue

            visited_nodes += 1

            if current_node == end:
                break

            for edge in self.graph.get(current_node, ()):
                if edge.is_closed:
                    continue

                if edge.target in blocked_nodes:
                    continue

                new_cost = current_cost + self._edge_cost(edge)

                if new_cost < distances.get(edge.target, inf):
                    distances[edge.target] = new_cost
                    minutes[edge.target] = minutes[current_node] + (
                        edge.base_minutes * max(edge.traffic_factor, 0.1)
                    )
                    kilometers[edge.target] = kilometers[current_node] + edge.distance_km
                    previous[edge.target] = current_node

                    counter += 1
                    heappush(queue, (new_cost, counter, edge.target))

        if end not in distances:
            raise ValueError(f"{start} ile {end} arasında uygun rota bulunamadı.")

        path = []
        node = end

        while node != start:
            path.append(node)
            node = previous[node]

        path.append(start)
        path.reverse()

        return RouteResult(
            path=tuple(path),
            total_minutes=round(minutes[end], 2),
            total_distance_km=round(kilometers[end], 2),
            total_cost=round(distances[end], 2),
            visited_nodes=visited_nodes
        )


def build_sample_graph() -> Dict[str, Tuple[Edge, ...]]:
    """
    Test ve demo amaçlı örnek şehir içi ulaşım grafiği.
    """

    return {
        "Merkez": (
            Edge("Üniversite", distance_km=5.0, base_minutes=8.0, traffic_factor=1.0),
            Edge("Otogar", distance_km=10.0, base_minutes=15.0, traffic_factor=1.0),
            Edge("Hastane", distance_km=4.0, base_minutes=7.0, traffic_factor=1.4),
        ),
        "Üniversite": (
            Edge("Otogar", distance_km=4.0, base_minutes=7.0, traffic_factor=1.0),
            Edge("Sanayi", distance_km=6.0, base_minutes=10.0, traffic_factor=1.2),
        ),
        "Hastane": (
            Edge("Otogar", distance_km=6.0, base_minutes=12.0, traffic_factor=1.0),
            Edge("Stadyum", distance_km=3.0, base_minutes=6.0, traffic_factor=1.1),
        ),
        "Sanayi": (
            Edge("Stadyum", distance_km=5.0, base_minutes=9.0, traffic_factor=1.0),
        ),
        "Otogar": (
            Edge("Stadyum", distance_km=4.0, base_minutes=8.0, traffic_factor=1.0),
        ),
        "Stadyum": tuple(),
    }


if __name__ == "__main__":
    optimizer = RouteSearchOptimizer(build_sample_graph())
    result = optimizer.shortest_path("Merkez", "Stadyum")

    print("En uygun rota:", " -> ".join(result.path))
    print("Toplam süre:", result.total_minutes, "dakika")
    print("Toplam mesafe:", result.total_distance_km, "km")
    print("Toplam maliyet:", result.total_cost)
    print("Ziyaret edilen düğüm sayısı:", result.visited_nodes)
```
