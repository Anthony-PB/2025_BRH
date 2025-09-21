"use client";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { useState } from 'react';
import { createUser, loginUser } from '@/api/auth';

export default function SignIn() {
    const [activeTab, setActiveTab] = useState('login');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [displayName, setDisplayName] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [emailError, setEmailError] = useState<string | null>(null);

    const validateEmail = (email: string): boolean => {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return emailRegex.test(email);
    };

    // Email related stuff
    const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const newEmail = e.target.value;
        setEmail(newEmail);
        
        if (emailError) {
            setEmailError(null);
        }
    };

    const handleSubmit = async () => {
        setLoading(true);
        setError(null);
        
        try {
            console.log('Submitting:', { email, password, displayName, activeTab });
            
            // Simulate API call
            if (activeTab === 'login') {
                await loginUser(email, password);
            } else {
                await createUser(email, password, displayName);
            }
            
            // On success, redirect or update UI as needed
            
            console.log('Success!');
        } catch (err) {
            setError('Authentication failed. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-beigebackground p-4">
            <Card className="w-full max-w-md">
                <CardHeader className="space-y-1">
                    <CardTitle className="text-2xl font-bold text-center">
                        Welcome to Name
                    </CardTitle>
                    <CardDescription className="text-center">
                        {activeTab === 'login' ? 'Sign in to your account' : 'Create a new account'}
                    </CardDescription>
                </CardHeader>
                
                <CardContent>
                    <div className="flex mb-6">
                        <button
                            type="button"
                            onClick={() => setActiveTab('login')}
                            className={`flex-1 py-2 px-4 text-sm font-medium border-b-2 transition-colors ${
                                activeTab === 'login'
                                    ? 'border-blue-500 text-blue-600'
                                    : 'border-transparent text-gray-500 hover:text-gray-700'
                            }`}
                        >
                            Sign In
                        </button>
                        <button
                            type="button"
                            onClick={() => setActiveTab('register')}
                            className={`flex-1 py-2 px-4 text-sm font-medium border-b-2 transition-colors ${
                                activeTab === 'register'
                                    ? 'border-blue-500 text-blue-600'
                                    : 'border-transparent text-gray-500 hover:text-gray-700'
                            }`}
                        >
                            Sign Up
                        </button>
                    </div>

                    {error && (
                        <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-600 rounded-md text-sm">
                            {error}
                        </div>
                    )}

                    <div className="space-y-4">
                        {activeTab === 'register' && (
                            <div>
                                <label htmlFor="displayName" className="block text-md font-semibold text-gray-700 mb-1">
                                    Display Name
                                </label>
                                <input
                                    id="displayName"
                                    type="text"
                                    value={displayName}
                                    onChange={(e) => setDisplayName(e.target.value)}
                                    required={activeTab === 'register'}
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                    placeholder="Your display name"
                                />
                            </div>
                        )}

                        <div>
                            <label htmlFor="email" className="block text-md font-semibold text-gray-700 mb-1">
                                Email Address
                            </label>
                            <input
                                id="email"
                                type="email"
                                value={email}
                                onChange={handleEmailChange}
                                onBlur={() => {
                                    if (email && !validateEmail(email)) {
                                        setEmailError('Please enter a valid email address');
                                    } else {
                                        setEmailError(null);
                                    }  
                                }}
                                aria-invalid={emailError ? 'true' : 'false'}
                                aria-describedby="email-error"
                                required
                                className={`w-full px-3 py-2 border rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 ${
                                    emailError 
                                        ? 'border-red-300 focus:ring-red-500 focus:border-red-500' 
                                        : 'border-gray-300 focus:ring-blue-500 focus:border-blue-500'
                                }`}
                                placeholder="you@example.com"
                            />
                            {emailError && (
                            <p id="email-error" className="text-red-500 text-sm mt-1">
                                {emailError}
                            </p>
                            )}
                        </div>

                        <div>
                            <label htmlFor="password" className="block text-md font-semibold text-gray-700 mb-1">
                                Password
                            </label>
                            <input
                                id="password"
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                placeholder="••••••••"
                                minLength={6}
                            />
                        </div>
                        <div>
                            <label htmlFor="confirm-password" className="block text-md font-semibold text-gray-700 mb-1">
                                Confirm Password
                            </label>
                            <input
                                id="confirm-password"
                                type="password"
                                value={confirmPassword}
                                onChange={(e) => setConfirmPassword(e.target.value)}
                                required
                                className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                placeholder="••••••••"
                                minLength={6}
                            />
                        </div>

                        {activeTab === 'register' && (
                            <div className="text-sm text-gray-600">
                                By creating an account, you agree to our Terms of Service and Privacy Policy.
                            </div>
                        )}

                        {activeTab === 'login' && (
                            <div className="text-right">
                                <button
                                    type="button"
                                    className="text-md font-semibold text-blue-600 hover:text-blue-500"
                                    onClick={() => console.log('Forgot password clicked')}
                                >
                                    Forgot your password?
                                </button>
                            </div>
                        )}

                        <button
                            type="button"
                            onClick={handleSubmit}
                            disabled={loading}
                            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-md font-semibold text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                        >
                            {loading ? (
                                <div className="flex items-center">
                                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                                    Processing...
                                </div>
                            ) : (
                                activeTab === 'login' ? 'Sign In' : 'Create Account'
                            )}
                        </button>
                    </div>
                </CardContent>
            </Card>
        </div>
    );
}