
<template>
  <div class="container py-5">
    <div class="row">
      <div class="col-lg-3">
        <CourseFilter @category-updated="filterCourse" />
      </div>
      <div class="col-lg-9">
        <CourseList :courses = 'filteredCourses' />
      </div>

    </div>
  </div>

</template>


<script>

  import CourseList from '@/components/CourseList.vue';
  import CourseFilter from '@/components/CourseFilter.vue';
  // import { courses } from '../tem-data'

  import axios from 'axios'

  export default {
    name: 'CoursesPage',
    components: {
      CourseList,
      CourseFilter
    },
    data(){
      return {
        courses: null,
        filteredCourses: null
      }
    },
  created(){
    this.getCourses()
  },

    methods:{
      getCourses(){
        axios.get("http://127.0.0.1:8000/courses/api")
          .then(response => {
            this.courses = response.data;
            this.filteredCourses = response.data;
          })
      },
      
      filterCourse(selectedCategory){
        if(selectedCategory.length == 0 ){
          this.filterCourse = this.courses
        }else{
        this.filteredCourses = this.courses.filter(course =>selectedCategory.includes(course.category_id) )
        }
      }
    }
  }
</script>