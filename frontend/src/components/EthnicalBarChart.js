import { D3SimpleBarChart } from '@yababay67/d3-adapter'

class EthnicalBarChart extends D3SimpleBarChart {

    setupData(data){
        return data.map(el => ({label: el[0], value: el[1][0]}))
            .filter(el => el.label != 'весь')
            .slice(0, 20)
    }

    adjust(d3, g, width, height, data){
        super.adjust(d3, g, width, height, data)
        const x = this._x
        const y = this._y
        const figure = this._figure
        d3.select(figure)
            .select('figcaption')
            .classed('text-end', true)
        g.selectAll(".label")        
            .data(data)
            .enter()
            .append("text")
            .style("fill", "#386890")
            .attr("x", (function(d) { return x(d.label) + x.bandwidth() / 2; }  ))
            .attr("y", function(d) { return y(d.value) - 25; })
            .attr("text-anchor", "middle")
            .attr("dy", ".75em")
            .text(function(d) { return d.value; });
    }
}

export default EthnicalBarChart
