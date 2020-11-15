U
    �Sx_M  �                   @   s�   d Z ddlmZ ddlmZ ddlmZ ddlmZ edej	dd�edej
d	d�ed
ejdd�edejdd�edejj�gZdS )am  suit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
�    )�admin)�url)�viewsz^$�home)�namez	^signup/$�signupz^boards/(?P<pk>\d+)/$�board_topicsz^boards/(?P<pk>\d+)/new/$�	new_topicz^admin/N)�__doc__Zdjango.contribr   Zdjango.conf.urlsr   �accountsr   Zaccounts_views�boardr   r   r   r	   �site�urls�urlpatterns� r   r   �D:\django\suit\suit\urls.py�<module>   s   �