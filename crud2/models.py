from django.db import models



class News(models.Model):
	title=models.CharField(max_length=150)
	content=models.TextField(blank=True)
	create_at=models.DateTimeField(auto_now_add=True)
	upload_at=models.DateTimeField(auto_now=True)
	photo=models.ImageField(upload_to='img/%Y/%m/%d/')
	is_published=models.BooleanField(default=True)


	def __str__(self):
		return self.title






# from crud2.models import News
# News.objects.all()
# news=_
# for item in news:
# 	print(item.title,item.content,item.is_published)

# News.objects.filter(title='News 3')
# News.objects.get(pk=2)

#ozgartirish kiritish-----

# News.objects.get(pk=4)
# news=_
# news.title='News 4'
# news.save()

#Delete---

# news5=News.objects.get(pk=5)
# news5.delete()


##---Sortirobka-----
# >>> News.objects.order_by('pk')
# <QuerySet [<News: News1>, <News: News 2>, <News: News 3>, <News: News 4>]>
# >>>

## -sortirobka teskari holat------
# >>> News.objects.order_by('-title')
# <QuerySet [<News: News1>, <News: News 4>, <News: News 3>, <News: News 2>]>
# >>>


# >>> News.objects.order_by('-pk')
# <QuerySet [<News: News 4>, <News: News 3>, <News: News 2>, <News: News1>]>
# >>>



## exclude() --

# >>> News.objects.exclude(pk=1)
# <QuerySet [<News: News 2>, <News: News 3>, <News: News 4>]>
# >>> News.objects.all()
# <QuerySet [<News: News1>, <News: News 2>, <News: News 3>, <News: News 4>]>
# >>> News.objects.exclude(pk=3)
# <QuerySet [<News: News1>, <News: News 2>, <News: News 4>]>
# >>> News.objects.exclude(title='News 3')
# <QuerySet [<News: News1>, <News: News 2>, <News: News 4>]>
# >>>