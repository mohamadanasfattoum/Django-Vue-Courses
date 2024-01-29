
<template>
  <div class="container">
    <h3>CourseFilter</h3>
    <form>
      <div class="mt-3">
        <label for="" class="my-2">Filter By Category </label>
        <div v-for="cat in category" :key="cat.id">
          <input type="checkbox"
          :value="cat.id"
          class="form-check-input me-2"
          :id="cat.id"
          v-model="selectedCategory"
          >
          <label :for="cat.id" class="form-label">{{ cat.name }}</label>
        </div>
      </div>
    </form>
  </div>

</template>

<script>

  export default {
    name: 'CourseFilter',
    data(){
      return{
        category:[
          {id:1, name:'Web Development'},
          {id:2, name:'Mobile Development'},
          {id:3, name:'AI Development'},
          
        ],
        selectedCategory: []
      }
    },
    watch:{
      selectedCategory(){
        this.$emit('category-updated', this.selectedCategory)
      }
    }
  }

</script>