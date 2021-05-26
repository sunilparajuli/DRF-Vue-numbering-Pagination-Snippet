

#example pagination parameter having total_pages from backend 
class PageNumberPaginationWithCount(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        response = super(PageNumberPaginationWithCount, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages  
        return response


#example list api view 
class VisitAPIView(generics.ListAPIView):
	pagination_class = PageNumbePaginationWithCount
	serializer_class = VisitSerializer

	def get_queryset(self):
		return Visit.objects.all()



#example url
urlspattern = [
	re_path(r'^api/v2/visits/', VisitAPIView.as_view(), name="visits_api"),
	
]
