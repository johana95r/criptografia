// muller
function f (x){
	return Math.pow(x,2) - Math.exp(-x)
}
function muller(x0,x1,x2,min_error,f){
	do{

		var fx0 = f(x0)
		var fx1 = f(x1)
		var fx2 = f(x2)

		var h0 = x1 - x0
		var h1 = x2 - x1

		var d0 = (fx1 - fx0) / (x1-x0)
		var d1 = (fx2 - fx1) / (x2-x1)

		var a = ( d1 - d0 ) / ( h1 + h0 )
		var b = ( a * h1 ) + d1
		var c = fx2

		var expPos = x2 +((-2*c)/(b+(Math.sqrt(Math.pow(b,2)-(4*a*c)))))
		var expNeg = x2 +((-2*c)/(b-(Math.sqrt(Math.pow(b,2)-(4*a*c)))))

		var x3 = (b>0) ? expPos : expNeg

		var error = Math.abs(((x3-x2)/x3)*100)

		x0 = x1
		x1 = x2
		x2 = x3

		console.log("-------------------" )
		console.log("fx0 " + fx0)
		console.log("fx1 " + fx1)
		console.log("fx2 " + fx2)
		console.log("h0 " + h0)
		console.log("h1 " + h1)
		console.log("d0 " + d0)
		console.log("d1 " + d1)
		console.log("a " + a)
		console.log("b " + b)
		console.log("c " + c)
		console.log("expPos " + expPos)
		console.log("expNeg " + expNeg)
		console.log("x3 " + x3)
		console.log("error " + error)

		console.log("-------------------")
	}while(min_error < error )
	alert(x3)

}
muller(2,0,-1,0.05,f)

// interpolacion_cuadratica

function f2 (x){
	return 2*Math.sin(x) - (Math.pow(x,2)/10)
}
function interpolacion_cuadratica(x0,x1,x2,min_error,f2){
	do{
	
		var fx0 = f2(x0)
		var fx1 = f2(x1)
		var fx2 = f2(x2)

		var x3 = (fx0 * ( (Math.pow(x1,2) - Math.pow(x2,2)) + fx1 * (Math.pow(x2,2) - Math.pow(x0,2)) + fx2 * (Math.pow(x0,2) - Math.pow(x1,2)) ) ) / ( 2 * fx0 * (x1 - x2) + 2*fx1 * (x2 - x0) + 2 * fx2 *(x0 - x1) )
		var fx3 = f2(x3)

		x0 = x1
		x1 = x3

		var error = Math.abs(((x3-x2)/x3)*100)
		console.log("-------------------")
		console.log("fx0 " + fx0)
		console.log("fx1 " + fx1)
		console.log("fx2 " + fx2)
		console.log("x3 " + x3)
		console.log("fx3 " + fx3)
		console.log("error " + error)
		console.log("-------------------")

	}while(min_error < error )
	alert (x3)

}
interpolacion_cuadratica(0,1,4,0.05,f2)