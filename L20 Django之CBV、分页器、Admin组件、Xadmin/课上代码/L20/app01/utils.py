class Paginator:
    def __init__(self, request, current_page, all_count, per_page=10, max_page_num=11):
        """
        封装分页相关数据
        :param current_page:  当前页码
        :param all_count:  数据库中的数据总条数
        :param per_page:   每个页面显示的数据条数
        :param max_page_num:  最多显示的页码个数
        :param num_pages:  通过总条数/每个页面显示的条数，求出总页数
        """
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = 1
        if current_page < 1:
            current_page = 1
        self.current_page = current_page
        self.all_count = all_count
        self.per_page = per_page

        # 计算总页数
        num_pages, temp = divmod(all_count, per_page)
        if temp:
            num_pages += 1
        self.num_pages = num_pages

        self.max_page_num = max_page_num  # 11
        self.page_count_half = int((self.max_page_num - 1) / 2)  # 5
        """
        self.num_pages=100
        per_page=8

        current_page =1     [0:8]
        current_page =2     [8:16]
        current_page =3     [16:24]
                            [(current_page-1)*per_page:current_page*per_page ]

        """

        import copy
        self.url_args = copy.deepcopy(request.GET)
        print(self.url_args.urlencode())

    @property
    def start(self):
        return (self.current_page - 1) * self.per_page

    @property
    def end(self):
        return self.current_page * self.per_page

    def page_html(self):
        # 如果总页数小于self.max_page_num(最多显示的页码个数)
        if self.num_pages <= self.max_page_num:
            page_start = 1
            page_end = self.num_pages + 1
        else:
            # 如果当前页码<=页面上最多显示11/2个页码时
            if self.current_page <= self.page_count_half:
                page_start = 1
                page_end = self.max_page_num + 1
            # 如果当前页码+最多显示11/2 大于 总页数时
            elif self.current_page + self.page_count_half > self.num_pages:
                page_start = self.num_pages - self.max_page_num + 1
                page_end = self.num_pages + 1
            else:
                page_start = self.current_page - self.page_count_half
                page_end = self.current_page + self.page_count_half + 1

        page_html_list = []

        # 首页
        self.url_args['page'] = 1
        first_page = '<nav aria-label="Page navigation"><ul class="pagination"><li><a href="?%s">首页</a></li>' % self.url_args.urlencode()
        page_html_list.append(first_page)

        # 上一页
        if self.current_page <= 1:
            prev_page = '<li class="disabled"><a href="javascript:void(0);">上一页</a></li>'
        else:
            self.url_args['page'] = self.current_page - 1
            prev_page = '<li><a href="?%s">上一页</a></li>' % self.url_args.urlencode()
        page_html_list.append(prev_page)

        # 显示页码
        for i in range(page_start, page_end):
            self.url_args['page'] = i
            if self.current_page == i:
                temp = '<li class="active"><a href="?%s">%s</a></li>' % (self.url_args.urlencode(), i)
            else:
                temp = '<li><a href="?%s">%s</a></li>' % (self.url_args.urlencode(), i)
            page_html_list.append(temp)

        # 下一页
        if self.current_page >= self.num_pages:
            next_page = '<li class="disabled"><a href="javascript:void(0);">下一页</a></li>'
        else:
            self.url_args['page'] = self.current_page + 1
            next_page = '<li><a href="?%s">下一页</a></li>' % self.url_args.urlencode()
        page_html_list.append(next_page)

        # 尾页
        self.url_args['page'] = self.num_pages
        last_page = '<li><a href="?%s">尾页</a></li></ul></nav>' % self.url_args.urlencode()
        page_html_list.append(last_page)

        return "".join(page_html_list)