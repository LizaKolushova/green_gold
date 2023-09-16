<template>
  <article class="news">
    <div class="article">
      <div class="article__header">
        <h1 class="article__title">{{ article.name }}</h1>
        <p class="article__date">{{ article.date }}</p>
      </div>
      <img
        class="article__image"
        :src="'images/' + article.full_image"
        alt="Фото с гольф площадки"
      />
      <p class="article__desc">{{ article.desc }}</p>
    </div>
  </article>
</template>

<script>
const axios = require("axios");

export default {
  name: "ArticlePage",
  created: function () {
    this.getArticle();
  },
  data: function () {
    return {
      articleId: this.$route.params.id,
      article: {},
    };
  },

  methods: {
    getArticle: function () {
      axios
        .get("/articles.json")
        .then((response) => {
          response.data.forEach((element) => {
            if (element.id == this.articleId) {
              this.article = element;
            }
          });
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    validate() {
      this.$refs.commentForm.validate();
    },
  },
};
</script>

<style lang="scss" scoped>
a{
  color: black;
}
.article {
  width: 65%;
  margin: 0 auto;
  font-style: normal;
  font-weight: 400;

  &__header {
    margin-top: 90px;
    margin-bottom: 70px;
  }
  &__title {
    font-size: 36px;
    line-height: 48px;
    font-weight: 400;
    text-align: center;
  }
  &__date {
    text-align: center;
    font-size: 20px;
    line-height: 27px;
  }
  &__desc {
    font-size: 24px;
    line-height: 34px;
    text-align: left;
    margin: 30px;
  }
  &__image {
    height: 430px;
    object-fit: cover;
    object-position: bottom;
    float: right;
    margin-left: 30px;
  }
}
.news {
  padding-bottom: 80px;
  background: rgb(255, 255, 255);
  background: linear-gradient(
    180deg,
    rgba(255, 255, 255, 1) 72%,
    rgba(134, 194, 50, 0.29744397759103647) 100%
  );
}
@media (max-width: 1186px) {
  .article {
    &__image {
      float: none;
      margin-left: 0px;
    }
  }
}
@media (max-width: 970px) {
  .article {
    width: 75%;
    margin: 0 auto;
    font-style: normal;
    font-weight: 400;

    &__header {
      margin-top: 80px;
      margin-bottom: 70px;
    }
    &__image {
      float: none;
    }
  }
}
@media (max-width: 575px) {
  .article {
    width: 100%;
    margin: 0 auto;
    font-style: normal;
    font-weight: 400;

    &__header {
      margin-top: 0px;
      margin-bottom: 30px;
      width: 100%;
      padding-top: 40px;
      padding-bottom: 64px;
      background-image: url(../assets/Man_mobile.png);
      background-repeat: no-repeat;
      background-size: cover;
      background-color: rgba(0, 0, 0, 0.2);
    }
    &__title {
      font-size: 20px;
      line-height: 27px;
      color: #fff;
    }
    &__date {
      font-size: 14px;
      line-height: 19px;
      color: #fff;
    }
    &__desc {
      font-size: 14px;
      line-height: 34px;
    }
    &__image {
      display: none;
    }
  }
}
</style>
