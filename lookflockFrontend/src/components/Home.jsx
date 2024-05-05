import React, { useEffect, useState } from 'react'
import Card from './Card'

let count = 10;
const Home = () => {
    const [data, setdata] = useState(null)
    const [loading, setloading] = useState(true)
    const fetchData = async (count = 10) => {
        try {
            const response = await fetch('http://127.0.0.1:8000/?count=' + count);
            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }
            const jsonData = await response.json();
            setdata(jsonData);
            setloading(false);
        } catch (error) {
            console.error('Error fetching data:', error);
            setloading(false);
        }
    };
    const handleButton = () => {
        count = count + 10;
        fetchData(count)
    }
    useEffect(() => {
        fetchData();
    }, []);
    if (loading) {
        return <div>Loading...</div>;
    }
    return (
        <div className='row m-4'>
            {data.map((item) => (
                <Card imageURL={item.imageURL} name={item.name} currentPrice={item.currentPrice} oldPrice={item.oldPrice} discount={item.discount} />
            ))}
            <div className='d-flex justify-content-center'>
                {data.length % 10 === 0 ? (
                    <button type='button' className='btn btn-primary' style={{ width: '90vw' }} onClick={handleButton}>Load More</button>) : (<div></div>)
                }
            </div>
        </div>
    )
}

export default Home