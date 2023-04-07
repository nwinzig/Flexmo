import React, {useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'
import './home.css'
function Home(){

    return (
        <div className='homePage'>
            <div className='homeLeft'>
                left
            </div>
            <div className='homeRight'>
                right
            </div>
        </div>
    )
}

export default Home
