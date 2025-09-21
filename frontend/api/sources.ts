export const getSources = async () => {
    const response = await fetch('http://localhost:8000/api/sources/');
    return response.json();
};

export const getSourceArticles = async (sourceId: string) => {
    const response = await fetch(`http://localhost:8000/api/sources/get/${sourceId}`);
    return response.json();
};

// Create source without auth for testing
export const createSource = async (sourceData: any) => {
    const response = await fetch('http://localhost:8000/api/sources/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(sourceData),
    });
    return response.json();
};