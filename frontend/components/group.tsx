interface GroupProps {
    title: string;
    description?: string;
    sourceCount?: number;
    sourcesIn: Array<string>;
}

export default function Group({ 
    title, 
    description, 
    sourceCount = 0, 
    sourcesIn 
}: GroupProps) {
    return (
        <div className="w-full max-w-lg py-6 px-6 border border-violet-400 rounded-lg bg-white shadow-sm">
            <div className="flex justify-between items-start mb-4">
                <div className="flex-1">
                    <h3 className="text-xl font-bold text-gray-900">{title}</h3>
                    {description && (
                        <p className="text-sm text-gray-600 mt-1">{description}</p>
                    )}
                </div>
                <span className="text-sm text-gray-500 bg-gray-100 px-2 py-1 rounded">
                    {sourceCount} source(s)
                </span>
            </div>
            
            <div className="space-y-2">
                <p className="text-sm font-medium text-gray-700">Sources:</p>
                <div className="flex flex-wrap gap-2">
                    {sourcesIn.slice(0,5).map((source, index) => (
                        <span 
                            key={index}
                            className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded-full"
                        >
                            {source}
                        </span>
                    ))}
                </div>
            </div>
        </div>
    );
}