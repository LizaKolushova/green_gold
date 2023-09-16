<template>
    <div class="footer_menu">
            <div class="text_menu">
                <p class="paragraph_small">FOLLOW THE FLOCK</p>
                <p class="paragraph_large">Exclusive offers, a heads up on new things, and sightings of Allbirds in the wild. Oh, we have cute sheep, too. #weareallbirds</p>
            </div>
            <div class="help_menu">
                <p class="paragraph_menu">Связаться с нами</p>
                <ul class="help_links">
                    <li class="help"><a class="cont" href="tel:1-888-963-8944">1-888-963-8944</a></li>
                    <li class="help"><a class="cont" href="tel:1-814-251-9966">1-814-251-9966 (Text)</a></li>
                    <li class="help"><a class="cont" href="mailto:help@allbirds.com">help@allbirds.com</a></li>
                    <li class="help"><a class="cont" href="#">Returns/Exchanges</a></li>
                    <li class="help"><a class="cont" href="#">FAQ/Contact Us</a></li>
                </ul>
            </div>
            <div class="shop_menu">
                <p class="paragraph_menu">Меню</p>
                <ul class="shop_links">
                    <li class="shop"><router-link class="cont" to="/">Главная</router-link></li>
                    <li class="shop"><router-link class="cont" to="/articles">Новости</router-link></li>
                    <li class="shop"><router-link class="cont" to="/articles/1">Новость недели</router-link></li>
                    <li class="shop"><router-link class="cont" to="/registration">Вступить в клуб</router-link></li>
                    <li class="shop"><router-link class="cont" to="/login">Войти</router-link></li>
                </ul>
            </div>
    </div>
</template>
<script>
export default {

};
</script>
<style>
* {
	margin: 0;
	padding: 0;
}
.cont{
    color: white;
}
.footer_menu{
    display: flex;
    align-items: flex-start;
    background-color: #0e2431;
    padding-left: 10%;
    padding-top: 60px;
    height: 380px;
    justify-content: space-around;
}
.paragraph_large{
    font-size: 14px;
    line-height: 21px;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 500;
    color: white;
    text-align: left;
    margin-top: 25px;
    width: 270px;
}
.paragraph_small{
    font-size: 14px;
    line-height: 21px;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 500;
    color: white;
    text-align: left;
}
.text_menu{
    width: 333px;
    height: 319px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.paragraph_menu{
    font-size: 14px;
    line-height: 21px;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 500;
    color: white;
    text-align: left;
}
.help_menu{
    width: 333px;
    height: 319px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.help_links{
    margin-top: 25px;
}
.help{
    font-size: 16px;
    line-height: 12px;
    letter-spacing: 0.5px;
    margin-bottom: 16px;
    list-style-type: none;
    display: flex;
}
.shop_menu{
    width: 333px;
    height: 319px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}
.shop_links{
    margin-top: 25px;
}
.shop{
    font-size: 16px;
    line-height: 12px;
    letter-spacing: 0.5px;
    margin-bottom: 16px;
    list-style-type: none;
    display: flex;
}
</style>