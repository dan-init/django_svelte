function testResultsData(data) {
    const [testResultsRaw] = data;

    return  {
        resultID: testResultsRaw.id,
        resultName: testResultsRaw.test_name,
    }
};

export default {
    testResultsData,
}