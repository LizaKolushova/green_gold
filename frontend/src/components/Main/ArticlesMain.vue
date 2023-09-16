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
        <button class="news-card__read-more-btn">
          <router-link :to="{ name: 'articleId', params: { id: article.id } }">
            Перейти
          </router-link>
        </button>
      </article>
    </div>
    </section>
</template>

<script>
const axios = require("axios");

export default {
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
        .get("/articles_small.json")
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
a{
  color: black;
}
.articles {
  display: flex;
  flex-direction: column;
  padding-top: 10vh;
  row-gap: 5vh;
  background-repeat: repeat;
  &__title {
    font-style: normal;
    font-weight: 400;
    line-height: 48px;
    font-size: 2rem;
    text-align: center;
  }
  &__news {
    display: grid;
    grid-template-columns: repeat(3, auto);
    justify-content: center;
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
  &__content {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    // width: 230px;
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
    background: rgba(97, 137, 47, 0.3);
    backdrop-filter: blur(2.5px);
    border-radius: 5px;
    margin-top: auto;
    padding: 10px 70px;
  }
}
</style>
