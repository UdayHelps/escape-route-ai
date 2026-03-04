async function loadRoutes(){

let origin=document.getElementById("origin").value

let res=await fetch(`/escape_routes?origin=${origin}`)

let data=await res.json()

let table=document.getElementById("table")

table.innerHTML=`<tr>
<th>Destination</th>
<th>Active Flights</th>
</tr>`

data.forEach(r=>{

table.innerHTML+=`
<tr>
<td>${r.destination}</td>
<td>${r.active_flights}</td>
</tr>
`

})

}
