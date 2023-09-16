<template>
    <section class="section_banner">
          <div class="content">
            <h2 class="heading_banner">Green Gold</h2>
            <p class="paragraph_banner">Гольф клуб, который не оставит вас равнодушным</p>
            <button class="see-more"><router-link to="/about" class="btn-see-more">Узнать больше</router-link></button>
          </div>
    </section> 
</template>

<script>
export default {
 
};
</script>
<style scoped>
.section_banner{
    background-image: url(../../assets/golf_place.png);
    background-size: cover;
    height: 700px;
}
.content{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 200px 0px 0px 300px;
}
.heading_banner{
    font-weight: 400;
    font-size: 50px;
    line-height: 53px;
    color: white;
}
.paragraph_banner{
    font-weight: 300;
    font-size: 25px;
    color: white;
    margin-top: 20px;
}
.see-more{
    border: none;
    background: #a7a7a750;
    backdrop-filter: blur(2.5px);
    border-radius: 5px;
    padding: 15px 0;
    margin-top: 50px;
}
.btn-see-more{
    color: white;
    font-weight: 300;
    font-size: 18px;
    padding: 15px 50px;
}

</style>