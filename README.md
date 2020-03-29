# Accessing an outer class from an inner class in Python

From my answer over at https://stackoverflow.com/a/60908562/8142307

**An [excerpt](https://stackoverflow.com/questions/2024566/how-to-access-outer-class-from-an-inner-class/60908562#comment57997025_2024566) describing the scenario:**

> An example of this scenario could be having a class with sub-classes that need to access the outer class,
as normal, but then needing to create another class (top level) derived from the first class. In that case,
the second class's sub-classes would try to access the parent using self.<original_parent_name> and get the original class,
not the new class that they are a sub-class from.
I hope people reading this can visualise this difficult scenario and see the point of questions like this
