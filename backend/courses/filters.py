from django_filters import rest_framework as filters



class CourseFilter(filters.FilterSet): 
    category = filters.CharFilter(field_name='category_id',method='filter_py_category')


    def filter_py_category(self,queryset,name,value):
        url_categories= value.split(',')
        return queryset.filter(category__id__in=url_categories)