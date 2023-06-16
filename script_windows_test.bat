python uber.py  -reset_all

python uber.py -create_map "local_path_original.txt"

python uber.py -load_fix_element H1 "<e4,5> <e8,5>"
python uber.py -load_fix_element A1 "<e5,5> <e1,5>"
python uber.py -load_fix_element T5 "<e14,8> <e13,0>"
python uber.py -load_fix_element H4 "<e9,0> <e10,4>"
python uber.py -load_fix_element S10 "<e12,3> <e16,3>"
python uber.py -load_fix_element K1 "<e12,3> <e16,3>"


python uber.py -load_movil_element P1 "<e3,3> <e4,3>" 20000
python uber.py -load_movil_element P2 "<e9,0> <e10,4>" 40000
python uber.py -load_movil_element P3 "<e14,8> <e13,0>" 2500
python uber.py -load_movil_element P4 "<e7,50> <e11,50>" 0

python uber.py -load_movil_element C1 "<e3,0> <e6,4>" 200
python uber.py -load_movil_element C2  "<e9,0> <e10,4>" 50
python uber.py -load_movil_element C3  "<e7,49> <e11,51>" 50


python uber.py -create_trip P1 "<e7,2> <e8,3>"
python uber.py -create_trip P1 "<e11,2> <e12,2>"
python uber.py -create_trip P1 "<e15,1> <e16,1>"
python uber.py -create_trip P2 H4
python uber.py -create_trip P2 "<e7,50> <e11,50>"
python uber.py -create_trip P3 S10
python uber.py -create_trip P4 "<e7,100> <e11,0>"
