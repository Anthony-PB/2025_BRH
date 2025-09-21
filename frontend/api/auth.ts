const API_BASE_URL = 'http://localhost:8000/api';

export const createUser = async (displayName: string, email: string, password: string, confirmPassword: string) => {
    try {
        const response = await fetch(`${API_BASE_URL}/users/register/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email,
                password,
                password_confirm: confirmPassword,
                display_name: displayName,
            }),
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem('authToken', data.token);
            return { success: true, user: data.user, token: data.token };
        } else {
            return { success: false, error: data };
        }
    } catch (error) {
        return { success: false, error: 'Network error' };
    }
};

export const loginUser = async (email: string, password: string) => {
    try {
        const response = await fetch(`${API_BASE_URL}/users/login/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password }),
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem('authToken', data.token);
            return { success: true, user: data.user, token: data.token };
        } else {
            return { success: false, error: data.error || 'Login failed' };
        }
    } catch (error) {
        return { success: false, error: 'Network error' };
    }
};