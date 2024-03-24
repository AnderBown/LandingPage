import streamlit as st

def main():
    selected_page = st.sidebar.radio("Navigation", ["Accueil", "Avantages", "Modèle Économique", "Public Cible", "Jeu en streamlit"])

    if selected_page == "Accueil":
        st.image("logo.png", width=100)
        st.title("Projet de jeux en Python")

        st.markdown(
            """
            Ce jeu Flappy Bird réalisé en Python avec Pygame. Contrôlez l'oiseau pour éviter les tuyaux et marquer des points. Le jeu comprend des classes pour gérer les événements et l'interface, ainsi qu'une fonction de pause et de retour au menu principal après la fin du jeu.
            """
        )
        
        st.markdown(
            """
            L'oiseau deviendra de plus en plus rapides, ce qui rendra le jeu plus difficile.
            """
        )

        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image("flappy_bird_screenshot1.png", width=200, caption="Écran de démarrage")

        with col2:
            st.image("flappy_bird_screenshot2.png", width=200, caption="Interface de jeu")

        with col3:
            st.image("flappy_bird_screenshot3.png", width=200, caption="Écran de règlement")

    elif selected_page == "Avantages":
        st.title("Avantages")
        st.markdown(
            """
            - Amusant et addictif
            - Facile à jouer, difficile à maîtriser
            - Convient à tous les âges
            """
        )

    elif selected_page == "Modèle Économique":
        st.title("Modèle Économique")
        st.markdown(
            """
            Notre modèle économique repose sur la publicité intégrée. Le jeu est gratuit à télécharger et à jouer. Nous générons des revenus en affichant des annonces publicitaires dans l'interface du jeu, qui peuvent apparaître au démarrage, en pause ou à la fin du jeu.
            """
        )

        st.markdown(
            """
            Nous générons des revenus en fonction du taux de clics ou d'affichages des annonces, en collaborant avec plusieurs partenaires publicitaires pour obtenir différentes ressources publicitaires.
            """
        )

        st.markdown(
            """
            Nous nous engageons à garantir que les annonces n'interfèrent pas avec l'expérience de jeu des joueurs.
            """
        )

        st.image("ads.png", width=300, caption="Exemple de publicité")


    elif selected_page == "Public Cible":
        st.title("Public Cible")
        st.markdown(
            """
            Notre public cible comprend les amateurs de jeux mobiles de tous âges, en particulier ceux qui apprécient les jeux simples et addictifs.
            """
        )
    
    elif selected_page == "Jeu en streamlit":
        st.markdown(
    """
    Pour plus d'informations, visitez [notre site Web](https://3nrqmpupeun6zbujnghqfd.streamlit.app/).
    """
)

if __name__ == "__main__":
    main()
