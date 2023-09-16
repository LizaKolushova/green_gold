<template>
  <div class="news-main">
    <h2 class="news-main__title">Новости</h2>
    <div class="news-main__content">
      <article class="news-card" :key="1">
        <img class="news-card__image" alt="News Image" src="images/Man.png" />
        <div class="news-card__content">
          <p class="news-card__date">19 Октября 2022</p>
          <h2 class="news-card__title">What is Lorem Ipsum?</h2>
          <p class="news-card__description">
            Начало статьи, какой-то текст, бла бла бла бла бла бла бла бла бла
            бла
          </p>
        </div>
        <router-link
          class="news-card__read-more-btn"
          :to="{ name: 'articleId', params: { id: 1 } }"
        >
          Перейти
        </router-link>
      </article>
      <article class="news-card" :key="2">
        <img class="news-card__image" alt="News Image" src="images/Man2.png" />
        <div class="news-card__content">
          <p class="news-card__date">20 Октября 2023</p>
          <h2 class="news-card__title">Why do we use it?</h2>
          <p class="news-card__description">
            Начало статьи, какой-то текст, бла бла бла бла бла бла бла бла бла
            бла
          </p>
        </div>
        <router-link
          class="news-card__read-more-btn"
          :to="{ name: 'articleId', params: { id: 2 } }"
        >
          Перейти
        </router-link>
      </article>
      <article class="news-card" :key="3">
        <img class="news-card__image" alt="News Image" src="images/ball.png" />
        <div class="news-card__content">
          <p class="news-card__date">24 Октября 2023</p>
          <h2 class="news-card__title">Where does it come from?</h2>
          <p class="news-card__description">
            Начало статьи, какой-то текст, бла бла бла бла бла бла бла бла бла
            бла
          </p>
        </div>
        <router-link
          class="news-card__read-more-btn"
          :to="{ name: 'articleId', params: { id: 3 } }"
        >
          Перейти
        </router-link>
      </article>
    </div>
  </div>
</template>

<script>
// const axios = require("axios");

export default {
  components: {},
  name: "ArticleSlider",
  props: {
    msg: String,
  },
  // created: function () {
  //   this.articlesList();
  // },
  // data: function () {
  //   return {
  //     articles: [],
  //   };
  // },
  // methods: {
  //   articlesList: function () {
  //     axios
  //       .get("/articles.json")
  //       .then((response) => {
  //         this.articles = response.data;
  //       })
  //       .catch(function (error) {
  //         console.log(error);
  //       });
  //   },
  // },
};
</script>
<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&display=swap");
.news-main {
  display: flex;
  flex-direction: column;
  &__title {
    font-style: normal;
    font-weight: 400;
    font-size: 36px;
    line-height: 48px;
    text-align: center;
  }
  &__content {
    display: flex;
    flex-direction: row;
    justify-content: center;
  }
}
.news-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 30px;
  font-style: normal;
  max-width: 350px;
  --btn-background: rgba(97, 137, 47, 0.3);
  &__image {
    width: 350px;
    transform-origin: center;
    transform: scale(var(--img-scale));
    transition: transform 0.4s ease-in-out;
  }
  &__content {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
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
  .news-main {
    padding-top: 40px;
    &__title {
      font-size: 24px;
      line-height: 32px;
    }
    &__content {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  }
}
</style>