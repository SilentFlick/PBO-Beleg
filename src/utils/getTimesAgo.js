const units = [
  [1, "second(s)"],
  [60, "minute(s)"],
  [60 * 60, "hour(s)"],
  [60 * 60 * 24, "day(s)"],
  [60 * 60 * 24 * 7, "week(s)"],
  [60 * 60 * 24 * 30, "month(s)"],
  [60 * 60 * 24 * 365, "year(s)"],
];

const getTimesAgo = (date) => {
  const seconds = Math.floor(
    (new Date().getTime() - new Date(date).getTime()) / 1000
  );
  let bestUnit = units[0];
  for (const unit of units) {
    if (seconds >= unit[0]) {
      bestUnit = unit;
    }
  }
  const [divisor, label] = bestUnit;

  return Math.floor(seconds / divisor) + " " + label + " ago";
};

export default getTimesAgo;
