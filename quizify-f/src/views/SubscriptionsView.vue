<template>
    <main class="container py-5">
        <div class="text-center mb-4">
            <h2 class="">Unlock Your Learning Journey</h2>
            <p class="lead">Choose a subscription plan that suits your needs and accelerates your exam preparation.</p>
        </div>

        <button class="btn btn-lg btn-energetic w-100 mt-5" @click="initiateRazorpayPayment" v-if="order">Pay with
            Razorpay</button>
        <div class="row row-cols-1 row-cols-md-2 g-4 justify-content-center" v-else>
            <div class="col-md-4">
                <div class="card rounded-3 shadow-sm h-100">
                    <div class="card-header">
                        <h4 class="fw-bold">Monthly</h4>
                    </div>
                    <div class="card-body">
                        <h1 class="card-title">₹149<small class="text-body-secondary fw-light">/month</small>
                        </h1>
                        <br>
                        <ul class="list-unstyled mt-3">
                            <li>Access to timed questions</li>
                            <li>Instant feedback</li>
                            <li>Performance analytics</li>
                        </ul>
                        <button class="btn btn-lg btn-energetic w-100 mt-5" @click="subscribe({ name: 'Monthly' })">Select
                            Plan</button>
                    </div>
                </div>
            </div>

            <div class="col-md-4">
                <div class="card rounded-3 shadow-sm h-100">
                    <div class="card-header">
                        <h4 class="fw-bold">Annual</h4>
                    </div>
                    <div class="card-body">
                        <h1 class="card-title">₹1,499<small class="text-body-secondary fw-light">/year</small></h1>
                        <p class="card-text">Get 2 months free! Equivalent to ₹125/month.</p>
                        <ul class="list-unstyled mt-3">
                            <li>Access to timed questions</li>
                            <li>Instant feedback</li>
                            <li>Performance analytics</li>
                        </ul>
                        <button class="btn btn-lg btn-energetic w-100 mt-5" @click="subscribe({ name: 'Annual' })">Select
                            Plan</button>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>
  
<script setup lang="ts">
import { ref } from 'vue';
import api from '@/api';
interface Plan {
    name: string;
}
const order = ref(null)
const subscribe = async (plan: Plan) => {
    try {
        const response = await api.post('/subscriptions/', plan);
        order.value = response.data;
    } catch (error) {
        console.error('Error:', error);
    }
};


const initiateRazorpayPayment = () => {
    if (order.value) {
        const options = {
            key: 'rzp_test_475iY2MVZRT3Mf',
            amount: order.value.amount,
            currency: 'INR',
            order_id: order.value.razorpay_order_id,
            handler: async function (response) {
                await api.post('/subscriptions/payment/', response);
            },
            prefill: {
                name: 'Azhar',
                email: 'a@a.com',
                contact: '+919638634737'
            }
        };

        const razorpay = new Razorpay(options);
        razorpay.open();
    }
};
</script>




<style scoped>
.btn-energetic {
    background-color: #505CE8;
    border-color: #505CE8;
    color: white;
}


.btn-energetic:hover {
    background-color: #3943A8;
}


/* .btn-vibrant
.btn-energetic
.btn-cerulean
.btn-lively
.btn-azure
.btn-dynamic
.btn-cobalt
.btn-invigorating
.btn-sapphire
.btn-radiant */
</style>
  