<template>
  <section class="articles">
    <h1 class="articles__title">Новости</h1>
    <div class="articles__news">
      <article class="news-card" v-for="article in articles" :key="article.id">
        <img
          class="news-card__image"
          alt="News Image"
          :src="'images/' + article.preview_image"
        />
        <div class="news-card__content">
          <p class="news-card__date">{{ article.date }}</p>
          <h2 class="news-card__title">{{ article.name }}</h2>
          <p class="news-card__description">
            {{
              article.shortDesc
                ? article.shortDesc
                : "К сожалению, у данной статьи нет описания"
            }}
          </p>
        </div>
        <router-link
          class="news-card__read-more-btn"
          :to="{ name: 'articleId', params: { id: article.id } }"
        >
          Перейти
        </router-link>
      </article>
    </div>
  </section>
</template>


<script>
const axios = require("axios");
export default {
  name: "ArticlesPage",
  props: {
    // msg: String
  },
  created: function () {
    this.articlesList();
  },
  data: function () {
    return {
      articles: [],
    };
  },
  methods: {
    articlesList: function () {
      axios
        .get("/articles.json")
        .then((response) => {
          this.articles = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&display=swap");
a{
  color: black;
}
.articles {
  display: flex;
  flex-direction: column;
  padding-top: 90px;
  row-gap: 5vh;
  background-image: url(../assets/background.png);
  background-repeat: repeat;
  &__title {
    font-style: normal;
    font-weight: 400;
    line-height: 48px;
    font-size: 2rem;
    text-align: center;
  }
  &__news {
    margin: 0 135px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 2fr));
    justify-content: center;
    justify-items: center;
  }
}
.news-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-right: 30px;
  margin-left: 30px;
  margin-bottom: 100px;
  font-style: normal;
  width: 350px;
  --btn-background: rgba(97, 137, 47, 0.3);
  &__image {
    width: 350px;
    max-width: 100%;
    transform-origin: center;
    transform: scale(var(--img-scale));
    transition: transform 0.4s ease-in-out;
  }
  &__content {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding-left: 60px;
  }
  &__date {
    margin-top: 5px;
    font-weight: 400;
    font-size: 16px;
    line-height: 30px;
  }
  &__title {
    font-weight: 500;
    font-size: 24px;
    line-height: 30px;
    margin: 5px 0;
    text-align: left;
  }
  &__description {
    font-weight: 400;
    font-size: 16px;
    line-height: 20px;
    margin: 5px auto 25px auto;
    text-align: left;
  }
  &__read-more-btn {
    border: none;
    backdrop-filter: blur(2.5px);
    border-radius: 5px;
    margin-top: auto;
    padding: 10px 70px;
    background: var(--btn-background);
    transition: color 0.4s ease-out;
  }
}
.news-card:has(:hover, :focus) {
  --img-scale: 1.09;
  --btn-background: #61892f;
}
@media (max-width: 970px) {
  .articles {
    &__news {
      margin: 0 100px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
      justify-content: center;
    }
  }

  .news-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 5px;
    margin-left: 5px;
    margin-bottom: 35px;
    font-style: normal;
    width: 190px;
    --btn-background: rgba(97, 137, 47, 0.3);
    &__image {
      width: 190px;
      transform-origin: center;
      transform: scale(var(--img-scale));
      transition: transform 0.4s ease-in-out;
    }
    &__content {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      padding-left: 30px;
    }
    &__date {
      margin-top: 5px;
      font-size: 12px;
      line-height: 30px;
    }
    &__title {
      font-size: 16px;
      line-height: 30px;
    }
    &__description {
      font-size: 14px;
      line-height: 20px;
      margin: 5px auto 10px auto;
    }
    &__read-more-btn {
      padding: 5px 35px;
    }
  }
}
@media (max-width: 575px) {
  .articles {
    padding-top: 40px;
    &__title {
      font-size: 24px;
      line-height: 32px;
    }
  }
}
</style>
  