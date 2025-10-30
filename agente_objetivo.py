import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# =======================
# 1. Descripción del problema
# =======================
st.title("Simulación de Agente Basado en Objetivos")
st.markdown("""
### Descripción del Problema
Imaginemos un agente que debe desplazarse de una ciudad inicial a una ciudad objetivo en un mapa de ciudades.  
El agente conoce su posición actual y el objetivo, y debe decidir paso a paso hacia dónde moverse hasta alcanzarlo.  

Este ejemplo simula cómo un **Agente Basado en Objetivos** toma decisiones deliberadas para alcanzar su meta, moviéndose solo por rutas disponibles entre ciudades.
""")

# =======================
# 2. Algoritmo / Pseudocódigo
# =======================
st.markdown("""
### Algoritmo / Pseudocódigo

Este enfoque muestra la toma de decisiones deliberativa del agente basada en alcanzar un objetivo específico.
""")

# =======================
# 3. Definición del mapa (grafo)
# =======================
mapa_ciudades = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

ciudad_inicial = st.selectbox("Ciudad Inicial", list(mapa_ciudades.keys()))
ciudad_objetivo = st.selectbox("Ciudad Objetivo", list(mapa_ciudades.keys()))

# =======================
# 4. Función del agente
# =======================
def agente_basado_en_objetivo(mapa, inicio, objetivo):
    """
    Simula un agente basado en objetivos que se mueve hacia la meta.
    """
    camino = [inicio]
    actual = inicio
    visitadas = set()
    
    while actual != objetivo:
        visitadas.add(actual)
        vecinos = [c for c in mapa[actual] if c not in visitadas]
        if not vecinos:
            st.warning("No hay camino disponible desde la ciudad actual.")
            return camino
        # Elegimos la primera ciudad disponible
        actual = vecinos[0]
        camino.append(actual)
    return camino

# =======================
# 5. Ejecución y visualización
# =======================
if st.button("Ejecutar Agente"):
    camino_recorrido = agente_basado_en_objetivo(mapa_ciudades, ciudad_inicial, ciudad_objetivo)
    st.success(f"Camino recorrido por el agente: {' -> '.join(camino_recorrido)}")

    # Visualización gráfica con NetworkX
    G = nx.Graph()
    for ciudad, vecinos in mapa_ciudades.items():
        for vecino in vecinos:
            G.add_edge(ciudad, vecino)

    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=800)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.5)

    # Resaltar el camino recorrido
    camino_aristas = list(zip(camino_recorrido[:-1], camino_recorrido[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=camino_aristas, width=3, edge_color="red")
    nx.draw_networkx_nodes(G, pos, nodelist=camino_recorrido, node_color="orange", node_size=900)

    plt.title("Mapa de Ciudades y Camino del Agente")
    st.pyplot(plt)

    # Mostrar paso a paso
    st.markdown("### Paso a Paso del Recorrido del Agente")
    for i, ciudad in enumerate(camino_recorrido):
        st.write(f"{i+1}. {ciudad}")

# =======================
# 6. Análisis final
# =======================
st.markdown("""
### Análisis Final

**Ventajas:**
- El agente toma decisiones deliberadas hacia un objetivo concreto.
- Fácil de entender e implementar.
- Útil para problemas de navegación, robótica y planificación de tareas.

**Limitaciones:**
- Requiere conocimiento completo del entorno.
- No maneja cambios dinámicos ni obstáculos imprevistos.
- Estrategia simple puede quedar atrapada si no hay caminos disponibles.

**Aplicaciones Reales:**
- Robots que navegan en interiores o exteriores.
- Videojuegos con NPCs que siguen rutas hacia objetivos.
- Sistemas de recomendación que buscan cumplir un objetivo específico.
""")
