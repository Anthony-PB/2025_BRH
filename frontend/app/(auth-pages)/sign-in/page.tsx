import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';

export default async function SignIn() {
    return (
        <div className='flex max-w-lg justify-center mx-auto h-screen items-center'>
            <Card className='flex-1 flex flex-col min-w-64'>
                <CardContent>Sign in</CardContent>
            </Card>
        </div>
        )
    ;
    }