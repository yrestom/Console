## **Console**

**Powerful Console for Frappe Backend**
It allows you to use the same as the `console` statement in Python as it is in JavaScript

### **How to Install**

1. `bench get-app https://github.com/yrestom/Console.git`
2. `bench build --app console`
3. `bench --site [your.site.name] install-app console`
4. `bench restart`

### How to use:

in python file:

```python
from console import console

my_list = ['foo', 4, 5, 'bar', 0.4]

console(my_list).loq()
```

In browser console:

```jsx
>(5) ["foo", 4, 5, "bar", 0.4]
```

### Supported  methods :

`log , table, warn, error, info, group, groupEnd, time, timeEnd, debug, trace, count`

### **License**

MIT