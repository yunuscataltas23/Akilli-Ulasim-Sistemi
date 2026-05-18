// Akilli Ulasim Sistemi - Neo4j Ornek Sorgulari
// Hazirlayan: Ayham Nawaf Hammoud

// 1. En Kisa Yolu Bulma (Trafik olmadan)
MATCH (baslangic:Kavsak {ad: 'A_Kavsagi'}), (varis:Kavsak {ad: 'B_Kavsagi'})
MATCH yol = shortestPath((baslangic)-[:YOL_BAGLANTISI*..15]-(varis))
RETURN yol, length(yol) AS durak_sayisi;

// 2. Trafik Agirligini Goz Onune Alan Optimal Rota (Dijkstra)
MATCH (baslangic:Kavsak {ad: 'A_Kavsagi'}), (varis:Kavsak {ad: 'B_Kavsagi'})
CALL gds.shortestPath.dijkstra.stream({
    nodeProjection: 'Kavsak',
    relationshipProjection: {
        YOL: {
            type: 'YOL_BAGLANTISI',
            properties: 'trafik_agirligi',
            orientation: 'UNDIRECTED'
        }
    },
    sourceNode: baslangic,
    targetNode: varis,
    relationshipWeightProperty: 'trafik_agirligi'
})
YIELD index, sourceNode, targetNode, totalCost, nodeIds, costs
RETURN gds.util.asNode(sourceNode).ad AS Baslangic, 
       gds.util.asNode(targetNode).ad AS Hedef, 
       totalCost AS Tahmini_Trafik_Maliyeti;
