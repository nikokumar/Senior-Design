import React from 'react';
import Plot from 'react-plotly.js';
import ButtonAppBar from './Navbar';

class LivePriceChart extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      stockChartXValues: [],
      stockChartYValues: []
    }
  }

  componentDidMount() {
    this.fetchStock();
  }

  fetchStock() {
    const pointerToThis = this;
    console.log(pointerToThis);
    const API_KEY = 'I1FO9LD96BAGAFQ2';
    let StockSymbol = 'TXN';
    let API_Call = `https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=${StockSymbol}&outputsize=compact&apikey=${API_KEY}`;
    let stockChartXValuesFunction = [];
    let stockChartYValuesFunction = [];

    fetch(API_Call)
      .then(
        function(response) {
          return response.json();
        }
      )
      .then(
        function(data) {
          console.log(data);

          for (var key in data['Time Series (Daily)']) {
            stockChartXValuesFunction.push(key);
            stockChartYValuesFunction.push(data['Time Series (Daily)'][key]['1. open']);
          }

          // console.log(stockChartXValuesFunction);
          pointerToThis.setState({
            stockChartXValues: stockChartXValuesFunction,
            stockChartYValues: stockChartYValuesFunction
          });
        }
      )
  }

  render() {
    return (
        <html>
      <ButtonAppBar/>
      <div  className = "cardPadder" align = "center">
        <Plot
          data={[
            {
              x: this.state.stockChartXValues,
              y: this.state.stockChartYValues,
              type: 'scatter',
              mode: 'lines+markers',
              marker: {color: 'red'},
            }
          ]}
          layout={{width: 900, height: 540, title: '$TXN Price Chart'}}
        />
      </div>
      </html>
    )
  }
}

export default LivePriceChart;