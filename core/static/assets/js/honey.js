/*

=========================================================
* New Bee -  Dashboard
=========================================================


=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. Please contact us to request a removal. Contact us if you want to remove it.

*/
async function getData() {
    const data = await d3.csv('/app/data.csv')
}

getData()

async function draw() {
    const dataset = await d3.csv("app/data.csv") 
}

draw()


const divBrowser = document.querySelector('div')
const divD3 = d3.select('#tagname') // insert name of tag
                .data(data)