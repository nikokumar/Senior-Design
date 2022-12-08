import React from "react";
import { DateRangePicker } from "materialui-daterange-picker";

const RangeField = (props) => {
  const [open, setOpen] = React.useState(true);
  const [dateRange, setDateRange] = React.useState({});
  const toggle = () => setOpen(!open);


  return (
    <div>
    <input className = "btn2" onFocus={() => setOpen(!open)} 
    placeholder={`${open ? "Close" : "Open"} Date Selector`}
    />
    <DateRangePicker
      open={open}
      toggle={toggle}
      minDate={"01/01/1900"}
      maxDate={"01/01/2300"}
      onChange={(range) => {
        console.log(range);
        setDateRange(range);
      }}
      initialDateRange={dateRange}
    />
    </div>
   
  );
};

export default RangeField;