## Welcome to yuqie's GitHub Pages

Some scripts used in [VASP](https://www.vasp.at/), which are mostly based on [python](https://www.python.org/) and [pymatgen](https://pymatgen.org/pymatgen.analysis.phase_diagram.html).


# learn python
1. Function：Arbitrary Number of Parameters
   def arithmetic_mean(first, *values):
       pass
       return
    if you have a list of numerical values： arithmetic_mean(*x)
     *  will "unpack" or singularize the list.
2. [pickle & shelve in python](https://www.python-course.eu/python3_file_management.php/)

   *city, day, time = line.split()
   join(city)
   City names can consist of multiple words like "Salt Lake City". 
   That is why we have to use the asterisk in the line, in which we split a line. 
   So city will be a list with the words of the city, e.g. ["Salt", "Lake", "City"]. 
   " ".join(city) turns such a list into a "proper" string with the city name, i.e. in our example "Salt Lake City".
