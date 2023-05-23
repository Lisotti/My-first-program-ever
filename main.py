def main():
    nombre=raw_input ("Cual es tu nombre? ")
    print "hola ",nombre
    vivis=raw_input ("En que ciudad vivis? ")
    print "Yo tambien vivo en",vivis
    resanio=2013
    resmes=8
    resdia=25
    dias=0
    preganio=input ("En que anio naciste? ")
    mesnac=input ("En que mes naciste? ")
    dianac=input ("Que dia naciste? ")
    if (dianac>resdia):
        dias=dias+(dianac-resdia)
    elif (dianac<resdia):
        dias=dias+((dianac+30)-resdia)
        mesnac=mesnac-1
    if (mesnac>resmes):
        dias=dias+(30*(mesnac-resmes))
    elif (mesnac<resmes):
        dias=dias+(30*((mesnac+12)-resmes))
        preganio=preganio+1
    dias=dias+((resanio-preganio)*365)
    print "tu tienes ",dias/365," anios de edad"
    print "tu tienes ",dias,"dias vividos"
    print "tu tienes ",dias*24, "horas vividas"
    print "tu tienes ",dias*24*60, "minutos vividos"
    print "tu tienes ",dias*24*60*60, "segundos vividos"
    print "tu te pasaste " ,(dias*15)/(60*24)," dias sentado en el inodoro cagando"
    print "tu te pasaste " ,(dias*30)/(60*24),"dias baniandote"
    print "tu te cortaste las unias " ,(dias/7),"veces"