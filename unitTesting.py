from Identification import Identification


ident_A = Identification(0,0,10,10, 1, "Car", "A", 1)
ident_A_3 = Identification(1,1,1,1,1,"Car","A", 1)

ident_A_1 = Identification(-5,-5,10,10,1,"Car","A",1)
ident_A_2 = Identification(-5,-5,5,5,1,"Car","A", 1)
ident_B = Identification(5,5,10,10, 1, "Car", "B", 1)
ident_C = Identification(10,10,10,10, 1, "Car", "C", 1)
ident_D = Identification(11,11,10,10, 1, "Car", "C", 1)

a = Identification(0,1,3,1, 1, "asdasd", "asd", 1)
b = Identification(1,0,1,3, 1, "asdasd", "asd", 1)


assert(a.checkCollision(b))
assert(b.checkCollision(a))

assert(ident_A.checkCollision(ident_A_1))
assert(ident_A_1.checkCollision(ident_A))

assert(ident_A.checkCollision(ident_A_3))

assert(ident_A_3.checkCollision(ident_A)) #

assert(ident_A.checkCollision(ident_A_2))


assert(ident_A.checkCollision(ident_B))
assert(ident_B.checkCollision(ident_A))

assert(ident_A.checkCollision(ident_C))
assert(ident_C.checkCollision(ident_A))

assert(not ident_A.checkCollision(ident_D))
assert(not ident_D.checkCollision(ident_A))


a_1 = Identification(0,0, 1,1, 1, "asdasd", "asd", 1)
b_1 = Identification(0,1, 1,1, 1, "asdasd", "asd", 1)



assert(a_1.checkCollision(b_1))