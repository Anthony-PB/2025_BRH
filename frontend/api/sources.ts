const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || '/api';

export const getSources = async () => {
    const response = await fetch(`${API_BASE_URL}/sources/`);
    return response.json();
};

export const getSourceArticles = async (sourceId: string) => {
    const response = await fetch(`${API_BASE_URL}/sources/get/${sourceId}`);
    return response.json();
};

// Create source without auth for testing
export const createSource = async (sourceData: any) => {
    const response = await fetch(`${API_BASE_URL}/sources/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(sourceData),
    });
    return response.json();
};