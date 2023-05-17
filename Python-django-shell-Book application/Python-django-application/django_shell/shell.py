Traceback (most recent call last):
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/home/andrew/Code/derp/python/djangobooks/library/views.py", line 24, in authors_overview
    for row in author_stats:
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/query.py", line 320, in __iter__
    self._fetch_all()
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/query.py", line 1507, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/query.py", line 130, in __iter__
    for row in compiler.results_iter(
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1312, in results_iter
    results = self.execute_sql(
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 1348, in execute_sql
    sql, params = self.as_sql()
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 573, in as_sql
    extra_select, order_by, group_by = self.pre_sql_setup()
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 64, in pre_sql_setup
    self.setup_query()
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 55, in setup_query
    self.select, self.klass_info, self.annotation_col_map = self.get_select()
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 284, in get_select
    sql, params = self.compile(col)
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/sql/compiler.py", line 494, in compile
    sql, params = vendor_impl(self, self.connection)
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/expressions.py", line 25, in as_sqlite
    sql, params = self.as_sql(compiler, connection, **extra_context)
  File "/home/andrew/Code/derp/python/djangobooks/venv/lib/python3.8/site-packages/django/db/models/aggregates.py", line 118, in as_sql
    return sql, params + filter_params
TypeError: can only concatenate list (not "tuple") to list
Any ideas what’s causing that?



