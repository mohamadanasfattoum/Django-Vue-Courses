<template>
    <button class="btn btn-primary" @click="toggleDarkMode"> </button>

</template>



<script>
    export default {
        name: 'DarkMode',
        props: {
            darkMode: {
                type: Boolean , defaulte: false
            }
        },

        methods: {
            toggleDarkMode() {
                this.$emit('dark-mode-change' , )

            }
        }
    }


</script>