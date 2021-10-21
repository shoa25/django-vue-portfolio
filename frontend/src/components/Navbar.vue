<template>
<div class="NavDiv">
    <nav>
        <label class="logo">IQ Laud</label>
        <ul class="navItems">
            <li><a class="active" href="#">Home</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
            <li><a href="#">Get Started</a></li>
        </ul>

        <div class="container">
            <div @click="toggle()" class="hamburgerIcon">
                <div></div>
                <div></div>
                <div></div>
            </div>
        </div>
    </nav>
</div>
</template>

<script>
export default {
    data() {
        return {

        }
    },
    methods: {
        toggle() {
            document.querySelector(".navItems").classList.toggle("show")
        }
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Gayathri:wght@700&family=Lexend+Deca:wght@400;700&family=Mali:wght@400;700&family=Nunito:wght@400;600;700&family=Rubik:wght@400;600&display=swap');

* {
    padding: 0;
    margin: 0;
    text-decoration: none;
    list-style: none;
}

.hamburgerIcon div {
    width: 35px;
    height: 4px;
    background-color: rgb(255, 255, 255);
    margin: 7px 0;
    border-radius: 5px;
}

.container{
  position: relative;
  height: 100%;
  width: 50px;
  float: right;
  justify-content: center;
  align-items: center;
  display: flex;
  margin-right: 40px;
}

.hamburgerIcon {
    display: none;
    float: right;
    cursor: pointer;
    position: absolute;
}

nav {
    height: 80px;
    width: 100%;
    background: rgb(75, 59, 163);
    border-bottom: 1px solid rgb(46, 0, 83);
}

label.logo {
    font-size: 30px;
    font-weight: 400;
    color: #ffffff;
    margin: 7px 50px;
    font-family: 'Lexend Deca';
    padding: 10px;
    cursor: pointer;
}

.navItems {
    float: right;
    margin-right: 40px;
}

nav li {
    display: inline-block;
    margin: 0 8px;
    line-height: 75px;
}

nav a {
    color: #6aff96;
    font-size: 18px;
    text-transform: uppercase;
    border: 1px solid transparent;
    padding: 7px 10px;
    border-radius: 3px;
    font-family: 'Rubik', sans-serif;
}

a.active,
a:hover {
    transition: .2s;
    color: #ffdf75;
    border-bottom: 3px solid #ff5e00;
}

@media (max-width:1048px) {
    label.logo {
        font-size: 28px;
        margin-left: 40px
    }

    nav ul {
        margin-right: 20px;
    }

    nav a {
        font-size: 17px;
    }
}

@media (max-width:909px) {

    .hamburgerIcon {
        display: block;
    }

    .navItems {
        position: fixed;
        width: 100%;
        height: 100vh;
        background: rgb(24, 12, 37);
        top: 80px;
        left: -100%;
        text-align: center;
        transition: .3s;
    }

    nav li {
        display: block;
        margin: 50px 0;
        line-height: 30px;
    }

    nav a {
        font-size: 20px;

    }

    a.active,
    a:hover {
        border: none;
        color: #b9b4ff;
    }

    .show {
        left: 0;
    }
}
</style>
