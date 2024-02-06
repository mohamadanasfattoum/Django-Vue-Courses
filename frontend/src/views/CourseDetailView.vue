
<template>
  <div class="container">
    <div class="row my-5 ms-5">
      <div class="col-lg-5" >
        <img :src="course.image" class="image " alt="">
      </div>
      <div class="col-lg-7 ">
        <h2>{{ course.name }}</h2>
        <p>{{ course.category }}</p>
        <p>{{ course.price }} $</p>

        <form method="post" class="row mt-4">
          <div class="col-lg-6">
            <input type="number" class="form-control" value="1">
          </div>
          <div class="col-lg-6">
            <button class="btn btn-info">Add To Cart</button>
          </div>

        </form>
        
      </div>
    </div>
  </div>
</template>


<script>

  import { courses } from '../tem-data'
  import axios from 'axios'
  
  export default {
    name: 'CourseDetailPage',
    data(){
      return{
        course: null
      }
    },
    created(){
      this.getCourse()
    },

    methods:{
      getCourse(){
        const courses_id = this.$route.params.course_id
        axios.get(`http://127.0.0.1:8000/courses/${courses_id}/api`)
          .then(response => {
            this.course = response.data;
          })
      },
    }
  }
</script>


<style>
  .image {
    width: 500px;
    height: 300px;
  }
</style>