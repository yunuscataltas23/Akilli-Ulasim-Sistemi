```python
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


from src.route_search_optimizer import Edge, RouteSearchOptimizer, build_sample_graph


class TestRouteSearchOptimizer(unittest.TestCase):

    def test_shortest_path_returns_valid_route(self):
        optimizer = RouteSearchOptimizer(build_sample_graph())

        result = optimizer.shortest_path("Merkez", "Stadyum")

        self.assertEqual(result.path[0], "Merkez")
        self.assertEqual(result.path[-1], "Stadyum")
        self.assertGreater(result.total_minutes, 0)
        self.assertGreater(result.total_distance_km, 0)

    def test_algorithm_prefers_lower_cost_route(self):
        graph = {
            "A": (
                Edge("B", distance_km=3, base_minutes=5, traffic_factor=1.0),
                Edge("C", distance_km=2, base_minutes=4, traffic_factor=4.0),
            ),
            "B": (
                Edge("D", distance_km=3, base_minutes=5, traffic_factor=1.0),
            ),
            "C": (
                Edge("D", distance_km=1, base_minutes=2, traffic_factor=4.0),
            ),
            "D": tuple(),
        }

        optimizer = RouteSearchOptimizer(graph)
        result = optimizer.shortest_path("A", "D")

        self.assertEqual(result.path, ("A", "B", "D"))

    def test_closed_roads_are_not_used(self):
        graph = {
            "A": (
                Edge("B", distance_km=1, base_minutes=2, is_closed=True),
                Edge("C", distance_km=2, base_minutes=5),
            ),
            "B": (
                Edge("D", distance_km=1, base_minutes=2),
            ),
            "C": (
                Edge("D", distance_km=2, base_minutes=5),
            ),
            "D": tuple(),
        }

        optimizer = RouteSearchOptimizer(graph)
        result = optimizer.shortest_path("A", "D")

        self.assertEqual(result.path, ("A", "C", "D"))

    def test_blocked_nodes_are_not_used(self):
        graph = {
            "A": (
                Edge("B", distance_km=1, base_minutes=2),
                Edge("C", distance_km=2, base_minutes=5),
            ),
            "B": (
                Edge("D", distance_km=1, base_minutes=2),
            ),
            "C": (
                Edge("D", distance_km=2, base_minutes=5),
            ),
            "D": tuple(),
        }

        optimizer = RouteSearchOptimizer(graph)
        result = optimizer.shortest_path("A", "D", frozenset({"B"}))

        self.assertEqual(result.path, ("A", "C", "D"))

    def test_same_start_and_end_returns_single_node_path(self):
        optimizer = RouteSearchOptimizer(build_sample_graph())

        result = optimizer.shortest_path("Merkez", "Merkez")

        self.assertEqual(result.path, ("Merkez",))
        self.assertEqual(result.total_minutes, 0.0)
        self.assertEqual(result.total_distance_km, 0.0)

    def test_unknown_start_node_raises_error(self):
        optimizer = RouteSearchOptimizer(build_sample_graph())

        with self.assertRaises(ValueError):
            optimizer.shortest_path("Bilinmeyen Durak", "Stadyum")

    def test_unknown_end_node_raises_error(self):
        optimizer = RouteSearchOptimizer(build_sample_graph())

        with self.assertRaises(ValueError):
            optimizer.shortest_path("Merkez", "Bilinmeyen Durak")

    def test_unreachable_destination_raises_error(self):
        graph = {
            "A": (
                Edge("B", distance_km=1, base_minutes=2),
            ),
            "B": tuple(),
            "C": tuple(),
        }

        optimizer = RouteSearchOptimizer(graph)

        with self.assertRaises(ValueError):
            optimizer.shortest_path("A", "C")

    def test_cache_works_for_repeated_searches(self):
        optimizer = RouteSearchOptimizer(build_sample_graph())

        optimizer.shortest_path("Merkez", "Stadyum")
        before = optimizer.shortest_path.cache_info().hits

        optimizer.shortest_path("Merkez", "Stadyum")
        after = optimizer.shortest_path.cache_info().hits

        self.assertGreater(after, before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
```
