import LivePriceChart from './components/livePriceChart';
import Home from './components/Home';
import TechnicalAnalysis from './components/technicalAnalysis';
import FundamentalAnalysis from './components/fundamentalAnalysis';
import {
  BrowserRouter,
  Switch,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    
    <Switch>
     <Route exact path="/" component={Home} />
     <Route path="/predictionResults" component={LivePriceChart} />
     <Route path='/technicalAnalysis' component={TechnicalAnalysis} />
     <Route path='/fundamentalAnalysis' component={FundamentalAnalysis} />
   </Switch>
  
);}
export default App;
