"""
#-*-coding:utf-8-*-
@Project:manageSystem
@File:pagenation.py
@Author:闵麒良
@Time:2022/7/7 16:22

"""

"""
封装分页组件
"""
from django.utils.safestring import mark_safe
import copy
class pageNation(object):
    """
    初始化参数说明：
    request：请求对象
    data：查询到的符合条件的数据
    search_data：搜索框收索的关键字，解决收索情况下分页的BUG
    page_parm：分页请求的参数名称，例如：http://127.0.0.1:8000/phonenum/list/?page=2&q=
    page_size：每页显示的数据量
    plus：当前页分页按钮的两边显示的按钮数量
    """

    def __init__(self,request,data,search_data,page_parm="page",page_size=15,plus=5):

        page=request.GET.get(page_parm,"")
        if page.isdecimal():
            page=int(page)
        else:
            page=1
        self.page=page
        self.page_size=page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.data=data[self.start:self.end]
        total_count = data.count()
        total_page_count,div = divmod(total_count,page_size)
        if div:
            total_page_count += 1
        self.total_page_count=total_page_count
        self.plus=plus
        self.search_data=search_data

    #生成html标签
    def Html(self):
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
        else:
            if self.page < self.plus:
                start_page = 1
                end_page = 2 * self.plus
            else:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus
        # 分页按钮
        page_str_list = []
        # 首页
        first_page = '<li><a href="?page={}&q={}">首页</a></li>'.format(1,self.search_data)
        page_str_list.append(first_page)
        # 上一页
        if self.page > 1:
            pre = '<li><a href="?page={}&q={}">上一页</a></li>'.format(self.page - 1,self.search_data)
        else:
            pre = '<li><a href="?page={}&q={}">上一页</a></li>'.format(1,self.search_data)
        page_str_list.append(pre)

        for i in range(start_page, end_page + 1):
            if i == self.page:
                ele = '<li class="active"><a href="?page={}&q={}">{}</a></li>'.format(i,self.search_data,i)
            else:
                ele = '<li><a href="?page={}&q={}">{}</a></li>'.format(i,self.search_data,i)
            page_str_list.append(ele)
        # 下一页
        if self.page < self.total_page_count:
            next = '<li><a href="?page={}&q={}">下一页</a></li>'.format(self.page + 1,self.search_data)
        else:
            next = '<li><a href="?page={}&q={}">下一页</a></li>'.format(self.total_page_count,self.search_data)
        page_str_list.append(next)
        # 尾页
        last_page = '<li><a href="?page={}&q={}">尾页</a></li>'.format(self.total_page_count,self.search_data)
        page_str_list.append(last_page)
        search_string = """
                        <div style="width: 150px;margin-bottom: 20px;display: inline-block">
                            <form method="get">
                                <div class="input-group">
                                    <input type="text" class="form-control" placeholder="请输入页码" name="page">
                                    <span class="input-group-btn">
                                        <button class="btn btn-primary" type="submit">跳转</button>
                                    </span>
                                </div>
                            </form>
                        </div>
                        """
        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string


