import axios from "axios";
import parsers from "./parser";

async function testResultsData() {
    const response = await axios.get('http://localhost:8000/testresults/?format=json');

    const [results] = response.data;

    return parsers.parseTestResults(response.data)

}

export default {
    testResultsData,
};