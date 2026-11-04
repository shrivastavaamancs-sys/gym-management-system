import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm
from django.db.models import Q
from django.core.paginator import Paginator  # Paginator import karein


from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Aapka message successfully bhej diya gaya hai!")
            return redirect('home')
        else:
            messages.error(request, "Form mein kuch errors hain, kripya sahi details bharein.")
    else:
        form = ContactForm()
    
    return render(request, 'members/index.html', {'form': form})

# 1. Member List & Stats
def member_list(request):
    query = request.GET.get('q', '')
    if query:
        members = Member.objects.filter(Q(name__icontains=query) | Q(phone__icontains=query))
    else:
        members = Member.objects.all()
        
    total_members = Member.objects.count()
    active_members = Member.objects.filter(is_active=True).count()
    pending_fees = Member.objects.filter(fee_status='Pending').count()
    
    context = {
        'members': members,
        'total_members': total_members,
        'active_members': active_members,
        'pending_fees': pending_fees,
        'query': query,
    }
    return render(request, 'members/member_list.html', context)

# 2. Add Member with OTP Step 1 (Form Data save to Session & Redirect to OTP)
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            # Form data ko session mein store karo
            request.session['pending_member'] = request.POST.dict()
            
            # 6-digit OTP generate karo
            otp = str(random.randint(100000, 999999))
            request.session['generated_otp'] = otp
            
            # Terminal par OTP print hoga (Testing ke liye)
            print(log_msg := f"\n====================\n [GYM SYSTEM] ADD MEMBER OTP: {otp}\n====================\n")
            
            return redirect('verify_add_otp')
    else:
        form = MemberForm()
    return render(request, 'members/add_member.html', {'form': form})

# Add OTP Verification Step 2
def verify_add_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        saved_otp = request.session.get('generated_otp')
        
        if entered_otp == saved_otp:
            # OTP match ho gaya, ab database mein member save karo
            post_data = request.session.get('pending_member')
            form = MemberForm(post_data)
            if form.is_valid():
                form.save()
                
            # Session clear karo
            del request.session['pending_member']
            del request.session['generated_otp']
            return redirect('member_list')
        else:
            error = "Galat OTP! Kripya sahi OTP enter karein."
            return render(request, 'members/verify_otp.html', {'error': error, 'action_type': 'Add Member'})
            
    return render(request, 'members/verify_otp.html', {'action_type': 'Add Member'})

# 3. Edit Member
def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/edit_member.html', {'form': form})

# 4. Delete Member with OTP Step 1
def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        # Member ID session mein save karo
        request.session['delete_member_id'] = pk
        
        otp = str(random.randint(100000, 999999))
        request.session['generated_otp'] = otp
        
        print(f"\n====================\n [GYM SYSTEM] DELETE MEMBER OTP: {otp}\n====================\n")
        return redirect('verify_delete_otp')
        
    return render(request, 'members/delete_confirm.html', {'member': member})

# Delete OTP Verification Step 2
def verify_delete_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        saved_otp = request.session.get('generated_otp')
        
        if entered_otp == saved_otp:
            pk = request.session.get('delete_member_id')
            member = get_object_or_404(Member, pk=pk)
            member.delete()
            
            del request.session['generated_otp']
            del request.session['delete_member_id']
            return redirect('member_list')
        else:
            error = "Galat OTP! Dobara koshish karein."
            return render(request, 'members/verify_otp.html', {'error': error, 'action_type': 'Delete Member'})
            
    return render(request, 'members/verify_otp.html', {'action_type': 'Delete Member'})



def member_list(request):
    query = request.GET.get('q', '')
    if query:
        members_list = Member.objects.filter(Q(name__icontains=query) | Q(phone__icontains=query))
    else:
        members_list = Member.objects.all()
        
    # Pagination: Ek page par 5 members show honge
    paginator = Paginator(members_list, 5)
    page_number = request.GET.get('page')
    members = paginator.get_page(page_number)
        
    total_members = Member.objects.count()
    active_members = Member.objects.filter(is_active=True).count()
    pending_fees = Member.objects.filter(fee_status='Pending').count()
    
    context = {
        'members': members,
        'total_members': total_members,
        'active_members': active_members,
        'pending_fees': pending_fees,
        'query': query,
    }
    return render(request, 'members/member_list.html', context)