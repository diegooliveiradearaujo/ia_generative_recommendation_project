import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def start_rec():
    st.header("Generate your recommendations")

    model_name = "distilbert-base-uncased" 
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    def encode_text(texts):
        inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        return outputs.last_hidden_state.mean(dim=1)

    def recommend_movies(user_preferences, movie_database):
        # Encode user preferences
        user_embedding = encode_text([user_preferences])
        
        # Encode movie descriptions
        movie_descriptions = [movie['description'] for movie in movie_database]
        movie_embeddings = encode_text(movie_descriptions)
        
        # Compute similarity between user preferences and movie descriptions
        similarities = cosine_similarity(user_embedding, movie_embeddings).flatten()
        
        # Create a list of movies with their similarity scores
        recommendations = [(movie_database[i]['title'], similarities[i]) for i in range(len(movie_database))]
        
        # Sort recommendations by similarity score in descending order
        recommendations.sort(key=lambda x: x[1], reverse=True)
        
        return recommendations

    user_preferences = st.text_input("Write your text here: ")
    movie_database = [ {"movie_id": 101, "title": "Inception", "description": "A skilled thief, the absolute best in the dangerous art of extraction, is offered a chance to have his criminal history erased."},
    {"movie_id": 102, "title": "The Matrix", "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."},
    {"movie_id": 103, "title": "Mad Max: Fury Road", "description": "In a post-apocalyptic world, Max teams up with a group of rebels to overthrow a tyrannical warlord."},
    {"movie_id": 104, "title": "John Wick", "description": "A former hitman comes out of retirement to seek vengeance for the killing of his beloved dog."},
    {"movie_id": 105, "title": "The Grand Budapest Hotel", "description": "The misadventures of a hotel concierge and his apprentice as they become involved in the theft of a priceless painting."},
    {"movie_id": 106, "title": "Superbad", "description": "Two high school friends navigate a series of hilarious and awkward experiences as they try to enjoy their final days before graduation."},
    {"movie_id": 107, "title": "The Godfather", "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."},
    {"movie_id": 108, "title": "Pulp Fiction", "description": "The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption."},
    {"movie_id": 109, "title": "The Shawshank Redemption", "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."},
    {"movie_id": 110, "title": "Jurassic Park", "description": "During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok."},
    {"movie_id": 111, "title": "Interstellar", "description": "A group of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."},
    {"movie_id": 112, "title": "The Social Network", "description": "The story of Facebook's creation and the legal battles that followed its rise to global prominence."},
    {"movie_id": 113, "title": "La La Land", "description": "A jazz musician and an aspiring actress fall in love but struggle to maintain their relationship while pursuing their dreams."},
    {"movie_id": 114, "title": "Fight Club", "description": "An insomniac office worker forms an underground fight club with a soap salesman, leading to unexpected consequences."},
    {"movie_id": 115, "title": "The Dark Knight", "description": "Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice when a new criminal mastermind, the Joker, emerges."},
    {"movie_id": 116, "title": "The Lion King", "description": "A lion prince flees his kingdom after the death of his father, only to learn the true meaning of responsibility and bravery."},
    {"movie_id": 117, "title": "Spirited Away", "description": "A young girl, Chihiro, becomes trapped in a mysterious and magical world and must find a way to rescue her parents and return to her own world."},
    {"movie_id": 118, "title": "Forrest Gump", "description": "The presidencies of Kennedy and Johnson, the events of the Vietnam War, the Watergate scandal, and other historical events unfold from the perspective of an Alabama man with an IQ of 75."},
    {"movie_id": 119, "title": "The Usual Suspects", "description": "A small-time con artist is recruited for a heist by a mysterious figure known as Keyser Söze, leading to a series of unexpected revelations."},
    {"movie_id": 120, "title": "Gone Girl", "description": "A man becomes the prime suspect in the disappearance of his wife, unraveling a complex and dark mystery."},
    {"movie_id": 121, "title": "Eternal Sunshine of the Spotless Mind", "description": "After a painful breakup, a couple undergoes a procedure to erase memories of each other from their minds, only to discover they still have feelings for one another."},
    {"movie_id": 122, "title": "Her", "description": "A lonely writer develops an unlikely relationship with an operating system designed to meet his every need."},
    {"movie_id": 123, "title": "The Revenant", "description": "A frontiersman on a quest for survival and revenge after being left for dead by his own hunting team."},
    {"movie_id": 124, "title": "Gravity", "description": "Two astronauts work together to survive after an accident leaves them stranded in space."},
    {"movie_id": 125, "title": "The Big Lebowski", "description": "A laid-back Los Angeles slacker is drawn into a complex kidnapping scheme after being mistaken for a wealthy businessman with the same name."},
    {"movie_id": 126, "title": "Crazy, Stupid, Love.", "description": "A middle-aged husband's life changes dramatically when his wife asks for a divorce. He seeks to rediscover his manhood with the help of a newfound friend."},
    {"movie_id": 127, "title": "The Hangover", "description": "A bachelor party in Las Vegas turns into a wild and chaotic adventure when the groom-to-be goes missing."},
    {"movie_id": 128, "title": "Titanic", "description": "A romance blooms aboard the ill-fated ship Titanic, as a young couple from different social classes find love during the voyage."},
    {"movie_id": 129, "title": "Mean Girls", "description": "A teenage girl navigates the complex social hierarchy of a high school after moving from Africa to the United States."},
    {"movie_id": 130, "title": "The Proposal", "description": "A high-powered book editor forces her assistant to marry her to avoid deportation, leading to unexpected complications."},
    {"movie_id": 131, "title": "Step Brothers", "description": "Two grown men, who still live with their respective parents, are forced to live together as step brothers."},
    {"movie_id": 132, "title": "50 First Dates", "description": "A man falls in love with a woman who suffers from short-term memory loss, making him have to woo her every day."},
    {"movie_id": 133, "title": "Mission: Impossible - Fallout", "description": "Ethan Hunt and his team must track down stolen plutonium while being monitored by the CIA after a mission goes wrong."},
    {"movie_id": 134, "title": "Fast & Furious", "description": "An undercover cop infiltrates an underground racing circuit to investigate a series of hijackings."},
    {"movie_id": 135, "title": "Jumanji: Welcome to the Jungle", "description": "Four teenagers are sucked into a magical video game, and the only way out is to work together to finish the game."},
    {"movie_id": 136, "title": "Notting Hill", "description": "The life of a bookstore owner changes when a famous actress walks into his shop, and they begin a romance."},
    {"movie_id": 137, "title": "Love Actually", "description": "The story of multiple characters' romantic lives unfolds in the weeks leading up to Christmas."},
    {"movie_id": 138, "title": "Deadpool", "description": "A wisecracking mercenary gets a new lease on life after undergoing an experiment that leaves him with accelerated healing powers."},
    {"movie_id": 139, "title": "Guardians of the Galaxy", "description": "A group of intergalactic misfits band together to stop a cosmic threat and protect a powerful orb."},
    {"movie_id": 140, "title": "Pretty Woman", "description": "A wealthy businessman hires a prostitute to accompany him to social events, leading to an unexpected romance."}
    ]

    if st.button('Recommend'):
        recommendations = recommend_movies(user_preferences, movie_database)
        df = pd.DataFrame(recommendations)
        df.columns = ('Movie', 'Rate')
        styled_df = df.style.background_gradient(subset=['Rate'], cmap='YlGn')
        st.dataframe(styled_df)

    st.markdown(
    """
    <style>
    .footer-text {
        position: fixed;
        bottom: 35px;
        right: 10px;
        font-size: 16px;
        color: #888;
    }
    </style>
    <div class="footer-text">
        Developed by Diego Oliveira - AI Engineer
    </div>
    """,
    unsafe_allow_html=True
    )

if __name__ == "__main__":
    start_rec()
