import axios from "axios";
import parsers from "./parser";

async function testResultsData() {
    const response = await axios.get('http://localhost:8000/testresults/');

    return parsers.testResultsData(response.data)
}

export default {
    testResultsData,
};