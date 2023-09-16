<template>
    <div><Banner/>
    <section class="gentlemen_game">
        <h3 class="gentlemen_game__heading">Гольф - игра джентельменов</h3>
        <p class="gentlemen_game__paragraph">Уникальное отличие гольфа — в глубочайшей порядочности игроков как по отношению друг к другу, так и к самой игре. Здесь исключены любые фальсификации или обманы. Если кто позволит себе обманывать, просто будет исключен из гольф-сообщества. И, конечно, гольф — это игра про терпение, умение дожать эмоции, победить психологически.</p>  
    </section>
    <Articles/>
  </div>
</template>

<script>
import Banner from "@/components/Main/BannerMain";
import Articles from "@/components/Main/ArticlesMain";

export default {
  name: 'MainPage',
  components: {
    Banner,
    Articles,
  },
}
</script>

<style>
.gentlemen_game{
    height: 780px;
    background-image: url(../assets/background.png);
}
.gentlemen_game__heading{
    font-style: normal;
    font-weight: 400;
    font-size: 34px;
    line-height: 48px;
    padding-top: 200px;
}
.gentlemen_game__paragraph{
    font-weight: 400;
    font-size: 26px;
    line-height: 43px;
    text-align: center;
    margin: 50px 20%;
}
a{
  color: black;
}
</style>
