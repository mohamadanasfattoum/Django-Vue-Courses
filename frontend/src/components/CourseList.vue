<template>
<div class="row mt-5">
  <div class="col-lg-4" v-for="course in courses" :key="course.id">
    <div class="card mb-3">
      <img :src="course.image" class="card-img-top  image" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ course.name }}</h5>
        <p>{{ course.category }}</p>
        <p>{{ course.price }} $</p>
        <RouterLink class="btn btn-primary" :to="'/'+course.id">Course Detail</RouterLink>

      </div>
    </div>
  </div>

</div>
</template>



<script>

  export default {
    name: 'CourseList',
    props: ['courses']
  }
</script>

<style>
  .image {
    width: 300px;
    height: 150px;
  }
</style>

