# Measures

A measure is a mapping (function), from Group to Numeric Value (G -> R), where a Group is basically any (part of a) DataFrame. For example, if your DataFrame consists of three columns: Name, Country, Age, then one of the measures is *average Age across countries*.

By default, all numeric columns are Measures. But what if you want to extend this behavior, read this chapter to understand how to define your own measures.

If you work in pure `Rust`, you don't need to worry about how you create bespoke measures, since you are not bounded by GIL 

If you don't want all numeric columns to be Measures, you can provide your own list:

```python
{{#include ../examples/calculate/measure.py}}

ds.ui()
```