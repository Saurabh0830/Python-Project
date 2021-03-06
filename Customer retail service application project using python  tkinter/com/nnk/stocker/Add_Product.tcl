#############################################################################
# Generated by PAGE version 4.13
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI Black} -size 20 -weight bold -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font10
vTcl:font:add_font \
    "-family {Segoe UI Black} -size 14 -weight bold -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font11
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top37
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_3_0 $base.fra38
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9} 
    wm focusmodel $top passive
    wm geometry $top 538x603+650+150
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Add_Product"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra38 \
        -borderwidth 10 -relief groove -background {#c4632b} -height 585 \
        -width 515 
    vTcl:DefineAlias "$top.fra38" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra38
    label $site_3_0.lab39 \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -text {Add Product} 
    vTcl:DefineAlias "$site_3_0.lab39" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab40 \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -text {PNO :} 
    vTcl:DefineAlias "$site_3_0.lab40" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab42 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text {Name :} 
    vTcl:DefineAlias "$site_3_0.lab42" "Label2_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Quantity :} 
    vTcl:DefineAlias "$site_3_0.lab43" "Label2_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text {Price :} 
    vTcl:DefineAlias "$site_3_0.lab44" "Label2_3" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent45 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent45" "AddProduct_Pno" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent46 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent46" "AddProduct_Name" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent47 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent47" "AddProduct_Quantity" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent48 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black 
    vTcl:DefineAlias "$site_3_0.ent48" "AddProduct_Price" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but49 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command AddProduct_Save \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font11,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Save 
    vTcl:DefineAlias "$site_3_0.but49" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but50 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command AddProduct_Back \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font11,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Back 
    vTcl:DefineAlias "$site_3_0.but50" "Button1_7" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab39 \
        -in $site_3_0 -x 120 -y 30 -width 282 -relwidth 0 -height 46 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab40 \
        -in $site_3_0 -x 50 -y 130 -width 102 -relwidth 0 -height 36 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab42 \
        -in $site_3_0 -x 30 -y 180 -width 102 -height 36 -anchor nw \
        -bordermode inside 
    place $site_3_0.lab43 \
        -in $site_3_0 -x 0 -y 240 -width 132 -relwidth 0 -height 36 \
        -relheight 0 -anchor nw -bordermode inside 
    place $site_3_0.lab44 \
        -in $site_3_0 -x 30 -y 300 -width 102 -height 36 -anchor nw \
        -bordermode inside 
    place $site_3_0.ent45 \
        -in $site_3_0 -x 150 -y 130 -width 244 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent46 \
        -in $site_3_0 -x 140 -y 180 -width 244 -height 34 -anchor nw \
        -bordermode inside 
    place $site_3_0.ent47 \
        -in $site_3_0 -x 140 -y 240 -width 244 -height 34 -anchor nw \
        -bordermode inside 
    place $site_3_0.ent48 \
        -in $site_3_0 -x 140 -y 300 -width 244 -height 34 -anchor nw \
        -bordermode inside 
    place $site_3_0.but49 \
        -in $site_3_0 -x 160 -y 380 -width 86 -relwidth 0 -height 43 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but50 \
        -in $site_3_0 -x 290 -y 370 -width 86 -height 43 -anchor nw \
        -bordermode inside 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra38 \
        -in $top -x 10 -y 10 -width 515 -relwidth 0 -height 585 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top37 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

